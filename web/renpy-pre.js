/**
 * Ren'Py Web Deployment - Silent Shxyder Edition
 * Focus: Force-ignoring errors and displaying custom white header.
 */

// ============================================================
// 1. PREVENT CRASHES FROM MISSING FUNCTIONS (ReferenceErrors)
// ============================================================
window.onerror = (msg, src, line, col, err) => true;
window.onunhandledrejection = (e) => { e.preventDefault(); };

window.progress = function(done, total) { };
window.presplashEnd = function() {
    const loader = document.getElementById('shxyder-loader');
    if (loader) {
        loader.style.opacity = "0";
        setTimeout(() => loader.remove(), 1000);
    }
};

// ROOT CAUSE FIX: renpyinput_ returns empty string → JSONDecodeError
// Always return a valid non-empty JSON string
window.startInput = function(d) {
    let r = prompt(d || "Input:", "");
    const safe = JSON.stringify((r !== null && r !== "") ? r : " ");
    if (window._input_callback) window._input_callback(safe);
    return safe;
};
window.inputResult = function(x) {
    if (x === null || x === undefined || x === "") return JSON.stringify(" ");
    return typeof x === "string" ? x : JSON.stringify(x);
};
window.endInput = function() { };
window.webglContextLost = false;
window.webglContextRestored = false;
window.isFullscreen = function() { return !!document.fullscreenElement ? 1 : 0; };

Module = window.Module || { };
Module.preRun = Module.preRun || [ ];

// ============================================================
// 2. BRANDING & UI OVERRIDE
// ============================================================
(function() {
    const header = document.createElement('h1');
    header.id = "shxyder-loader";
    header.innerText = "Ported By Shxyder";
    document.body.appendChild(header);

    const style = document.createElement('style');
    style.innerHTML = `
        body, html { margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; background: black; font-family: sans-serif; }

        #shxyder-loader {
            position: absolute; top: 45%; width: 100%; text-align: center;
            color: white; font-size: 3rem; z-index: 10000;
            transition: opacity 1s ease; pointer-events: none; text-transform: uppercase;
        }

        #canvas {
            position: absolute; top: 0; left: 0; width: 100vw !important; height: 100vh !important;
            outline: none !important; z-index: 10; display: block;
        }
    `;
    document.head.appendChild(style);
})();

// ============================================================
// 3. CANVAS-LEVEL IGNORE CLICKER
// The Ren'Py error screen is drawn by SDL onto the canvas —
// not a DOM element. We must simulate real mouse events on
// the canvas at the pixel position of the "Ignore" button.
//
// In Ren'Py's exception screen the buttons sit in a row at
// the very bottom of the canvas (~94% down). "Ignore" is
// the second button, roughly 17% from the left edge.
// We also click several nearby X positions to handle
// different canvas sizes / DPI scaling.
// ============================================================

function clickCanvasAt(canvas, xRatio, yRatio) {
    const rect = canvas.getBoundingClientRect();
    const x = rect.left + rect.width  * xRatio;
    const y = rect.top  + rect.height * yRatio;
    const opts = { bubbles: true, cancelable: true, clientX: x, clientY: y, view: window };
    canvas.dispatchEvent(new MouseEvent('mousemove', opts));
    canvas.dispatchEvent(new MouseEvent('mousedown', opts));
    canvas.dispatchEvent(new MouseEvent('mouseup',   opts));
    canvas.dispatchEvent(new MouseEvent('click',     opts));
}

// "Ignore" button x positions to try (as fraction of canvas width)
// covering small, medium and large canvas widths
const IGNORE_X_RATIOS = [0.14, 0.17, 0.20, 0.23];
// Button row y position (fraction of canvas height)
const BUTTON_Y_RATIO  = 0.945;

setInterval(() => {
    const canvas = document.getElementById('canvas');
    if (!canvas) return;
    IGNORE_X_RATIOS.forEach(xr => clickCanvasAt(canvas, xr, BUTTON_Y_RATIO));
}, 500); // every 500ms — fast enough without hammering SDL

// ============================================================
// 4. ASSET LOADING & ENGINE PATCHING
// ============================================================
async function downloadAssets() {
    try {
        const resp = await fetch("file_list.json");
        const list = (await resp.json()).filter(f =>
            !["index.html", "renpy.js", "renpy-pre.js", "renpy.wasm", "game.zip"].includes(f)
        );

        for (const path of list) {
            if (path.includes('/')) {
                const parts = path.split('/');
                let cur = "";
                for (let i = 0; i < parts.length - 1; i++) {
                    cur += (cur ? "/" : "") + parts[i];
                    try { FS.mkdir("/" + cur); } catch(e) {}
                }
            }
            const fResp = await fetch(path);
            if (fResp.ok) {
                FS.writeFile("/" + path, new Uint8Array(await fResp.arrayBuffer()));
                if (path.endsWith("main.py")) FS.writeFile("/main.py", FS.readFile("/" + path));
            }
        }

        FS.writeFile('/game.zip', new Uint8Array([
            0x50,0x4b,0x05,0x06,0x00,0x00,0x00,0x00,
            0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
            0x00,0x00,0x00,0x00,0x00,0x00
        ]));

        window.presplashEnd();
    } catch (e) { }
}

Module.preRun.push(() => {
    const patcher = setInterval(() => {
        if (window.renpyAudio && window.renpyAudio.queue) {
            const oldQ = window.renpyAudio.queue;
            window.renpyAudio.queue = function(t, f, n, p, fd, ti, v) {
                if (v && typeof f === 'string') f = f.replace(/game\.zip\//g, '');
                try { return oldQ.call(this, t, f, n, p, fd, ti, v); } catch (e) { return; }
            };
            clearInterval(patcher);
        }
    }, 50);

    Module.addRunDependency('shxyder_load');
    downloadAssets().then(() => Module.removeRunDependency('shxyder_load'));
});

Module.canvas = document.getElementById('canvas');

window.addEventListener('mousedown', () => {
    if (Module.canvas) Module.canvas.focus();
    if (window.renpyAudio && window.renpyAudio.ctx) window.renpyAudio.ctx.resume();
}, true);