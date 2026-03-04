Module = window.Module || { };
Module.preRun = Module.preRun || [ ];

// Standard atExit fix
window.atExit = function() { };

(function () {
    const statusTextDiv = document.getElementById("statusTextDiv");
    function printMsg(s) {
        console.log(s);
        if (statusTextDiv) statusTextDiv.innerHTML += s + "<br>";
    }

    async function loadFolderAssets() {
        try {
            // 1. Setup the basic isolated directory
            try { FS.mkdir('/game'); } catch(e) {}
            const emptyZip = new Uint8Array([80, 75, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
            FS.writeFile('/game/game.zip', emptyZip);

            // 2. Fetch manifest
            const response = await fetch("file_list.json");
            const fileList = await response.json();

            printMsg("Injecting Python libraries...");

            for (let i = 0; i < fileList.length; i++) {
                const filePath = fileList[i];
                
                // Deep strip leading "game/"
                let strippedPath = filePath;
                while (strippedPath.startsWith("game/")) {
                    strippedPath = strippedPath.substring(5);
                }
                
                // We write everything to ROOT (/) instead of /game/ 
                // to make sure /lib/python3.12 is found by the engine
                const targetPath = "/" + strippedPath;
                
                const parts = targetPath.split('/');
                let currentDir = "";
                for (let j = 1; j < parts.length - 1; j++) {
                    currentDir += "/" + parts[j];
                    try { FS.mkdir(currentDir); } catch (e) {} 
                }

                const fileRes = await fetch(filePath);
                if (!fileRes.ok) continue;
                const buffer = await fileRes.arrayBuffer();
                
                FS.writeFile(targetPath, new Uint8Array(buffer));
            }

            // 3. Set Python Environment Variables
            // This tells the engine to look in OUR virtual /lib folder
            ENV['PYTHONHOME'] = '/';
            ENV['PYTHONPATH'] = '/lib/python3.12:/lib/python3.12/lib-dynload';
            
            printMsg("Python environment mapped. Booting...");
        } catch (e) {
            printMsg("<span style='color:red'>ERROR: " + e.message + "</span>");
        }
    }

    Module.preRun.push(() => {
        // Prepare storage and block /proc
        try {
            FS.mkdir('/proc');
            FS.mkdir('/proc/self');
            FS.mkdir('/proc/self/fd');
            FS.mkdirTree('/home/web_user/.renpy');
            FS.mount(IDBFS, {}, '/home/web_user/.renpy');
        } catch(e) {}

        Module.addRunDependency('folder_loader');
        loadFolderAssets().then(() => {
            Module.removeRunDependency('folder_loader');
        });
    });

    // Required Ren'Py hooks
    window.presplashEnd = () => { document.getElementById('presplash')?.remove(); };
    window.renpy_exec = function(py) {};
    window.setFullscreen = (e) => {};
    window._renpy_cmd_callback = function(r) {};
})();