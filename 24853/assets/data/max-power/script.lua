function onCreate()

makeAnimatedLuaSprite('topstage', 'chapters/chapter3/images/background/disco/changingstuff', -400, 250)
setScrollFactor('topstage', 0.9, 0.9)
addAnimationByPrefix('topstage', 'closed', 'doorclosed', 24, false)
objectPlayAnimation('topstage', 'closed', true)
setObjectOrder('topstage', 0)
addLuaSprite('topstage', false)

makeAnimatedLuaSprite('heroesdannce', 'chapters/chapter3/images/background/disco/changingstuffmaxapower', -400, 190)
setScrollFactor('heroesdannce', 0.9, 0.9)
addAnimationByPrefix('heroesdannce', 'normal', 'heroesbop', 24, false)
objectPlayAnimation('heroesdannce', 'normal', true)

makeAnimatedLuaSprite('toadboppers', 'chapters/chapter3/images/background/disco/changingstuff', -380, 1120)
setScrollFactor('toadboppers', 0.9, 0.9)
addAnimationByPrefix('toadboppers', 'boop', 'frontbop', 24, false)
objectPlayAnimation('toadboppers', 'boop', true)
addLuaSprite('toadboppers', true)

makeLuaSprite('blackbg', 'chapters/chapter2/images/background/std/blackbg', -400, -100)
setProperty('blackbg.alpha', 0.4);
addLuaSprite('blackbg', true)

makeLuaSprite('discoLight', 'chapters/chapter3/images/background/disco/discoLight', -1200, 50)
setProperty('discoLight.alpha', 0.6);
addLuaSprite('discoLight', true)

addLuaSprite('heroesdannce', false)
setObjectOrder('heroesdannce', 1)

setProperty('skipCountdown', true)

end

function onBeatHit()
objectPlayAnimation('toadboppers', 'boop', true)
objectPlayAnimation('heroesdannce', 'normal', true)
end

function onUpdate()
setProperty('discoLight.angle', getProperty('discoLight.angle') - 0.1)
end