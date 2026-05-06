
#include "UiRender.h"
#include "ResourceImport.h"
#include "raylib.h"

Texture2D ageTex, coinTex, backTex, sleepTex, smartTex, healthTex, jobTex;
Texture2D schoolTex, happyTex, relationTex, activityTex, assetTex, settingsTex;
Sound clickSnd, coinSnd;
Font fontBold, fontLight;

void loadAll() {
    Image ageIco = LoadImage("assets/images/age.png");
    ageTex = LoadTextureFromImage(ageIco);
    UnloadImage(ageIco);
    Image coinIco = LoadImage("assets/images/coin.png");
    coinTex = LoadTextureFromImage(coinIco);
    UnloadImage(coinIco);
    Image backIco = LoadImage("assets/images/back.png");
     backTex = LoadTextureFromImage(backIco);
    UnloadImage(backIco);
    Image smartIco = LoadImage("assets/images/smart.png");
    smartTex = LoadTextureFromImage(smartIco);
    UnloadImage(smartIco);
    Image healthIco = LoadImage("assets/images/health.png");
    healthTex = LoadTextureFromImage(healthIco);
    UnloadImage(healthIco);
    Image jobIco = LoadImage("assets/images/job.png");
    jobTex = LoadTextureFromImage(jobIco);
    UnloadImage(jobIco);
    Image schoolIco = LoadImage("assets/images/school.png");
    schoolTex = LoadTextureFromImage(schoolIco);
    UnloadImage(schoolIco);
    Image happyIco = LoadImage("assets/images/happy.png");
    happyTex = LoadTextureFromImage(happyIco);
    UnloadImage(happyIco);
    Image relationIco = LoadImage("assets/images/relation.png");
    relationTex = LoadTextureFromImage(relationIco);
    UnloadImage(relationIco);
    Image activityIco = LoadImage("assets/images/activity.png");
    activityTex = LoadTextureFromImage(activityIco);
    UnloadImage(activityIco);
    Image assetIco = LoadImage("assets/images/asset.png");
    assetTex = LoadTextureFromImage(assetIco);
    UnloadImage(assetIco);
    Image settingsIco = LoadImage("assets/images/settings.png");
    settingsTex = LoadTextureFromImage(settingsIco);
    UnloadImage(settingsIco);
    Image sleepIco = LoadImage("assets/images/sleep.png");
    sleepTex = LoadTextureFromImage(sleepIco);
    UnloadImage(sleepIco);

    clickSnd = LoadSound("assets/sound/click_sound.wav");
    coinSnd = LoadSound("assets/sound/coin_sound2.wav");

    fontBold = LoadFontEx("Inter_18pt-Black.ttf", 100, 0, 0);
    SetTextureFilter(fontBold.texture, TEXTURE_FILTER_BILINEAR);
    fontLight = LoadFontEx("Inter_18pt-Light.ttf", 100, 0, 0); 
    SetTextureFilter(fontLight.texture, TEXTURE_FILTER_BILINEAR);
}

void unloadAll() {
    UnloadTexture(coinTex);
    UnloadTexture(ageTex);
    UnloadTexture(backTex);
    UnloadTexture(sleepTex);
    UnloadTexture(smartTex);
    UnloadTexture(healthTex);
    UnloadTexture(jobTex);
    UnloadTexture(schoolTex);
    UnloadTexture(happyTex);
    UnloadTexture(relationTex);
    UnloadTexture(activityTex);
    UnloadTexture(assetTex);
    UnloadTexture(settingsTex);
    UnloadSound(clickSnd);
    UnloadSound(coinSnd);
    UnloadFont(fontBold);
    UnloadFont(fontLight);
    CloseAudioDevice();
    CloseWindow();
}
