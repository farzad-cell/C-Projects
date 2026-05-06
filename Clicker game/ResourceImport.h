#pragma once
#include "UiRender.h"
#include "raylib.h"



extern Texture2D coinTex;
extern Texture2D ageTex;
extern Texture2D backTex;
extern Texture2D sleepTex;
extern Texture2D smartTex;
extern Texture2D healthTex;
extern Texture2D jobTex;
extern Texture2D schoolTex;
extern Texture2D happyTex;
extern Texture2D relationTex;
extern Texture2D activityTex;
extern Texture2D assetTex;
extern Texture2D settingsTex;

extern Sound clickSnd;
extern Sound coinSnd;

extern Font fontBold;
extern Font fontLight;

void loadAll();
void unloadAll();
