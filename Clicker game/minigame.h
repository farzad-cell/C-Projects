#pragma once
#include "raylib.h"

extern float fatiguecount;

enum GameScreen { MENU, COIN_GAME, JOBSCRN, SCHOOLSCRN, ASSETSCRN , SETTINGSCRN, RELATIONSCRN, 
                  ACTIVITYSCRN };

const int coinUpgradeSize = 50;

struct GameData {
    double money = 0.00;
    double coinCost[coinUpgradeSize] = { 0.00, 0.50, 5.00, 50.00, 500.00, 5000.00 };
	double coinPower[coinUpgradeSize] = { 0.01, 0.02, 0.10, 1.00, 10.00, 100 };
    int coinIndex = 1;
    double coinRate = 0.01;
};


extern GameData coinData;

// Prototypes
void coinUpgrade(GameData& coinData, Sound clickSnd, float &fatiguecount);
float fatigueBar(float& fatiguecount);
bool rectangleHitbox(float xPos, float yPos, float width, float height);