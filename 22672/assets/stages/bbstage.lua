function onCreate()

	makeLuaSprite('stageback','stageback',-653,-200)
	setScrollFactor('stageback', 0.5, 0.5);
	scaleObject('stageback', 1.1, 1.1);

	makeLuaSprite('crowdback','crowdback',-650,0)
	setScrollFactor('crowdback', 0.5, 0.5);

	makeLuaSprite('cameosback','cameosback',-680,-200)
	setScrollFactor('cameosback', 0.5, 0.5);

	makeLuaSprite('audiencefront','audiencefront',-800,40)
	setScrollFactor('audiencefront', 0.8, 0.8);
	
	makeLuaSprite('stagefront','stagefront',-1000,-89)
	setScrollFactor('stagefront', 0.9, 0.9);
	scaleObject('stagefront', 1.2, 1.2);
   
	addLuaSprite('stageback', false);
    addLuaSprite('crowdback', false);
    addLuaSprite('cameosback', false);
	addLuaSprite('audiencefront', false);
	addLuaSprite('stagefront', false);
end

