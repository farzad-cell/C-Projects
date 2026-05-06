#include "engine/WindowSetup.h"
#include "core/ScreenController.h"
#include "databases/sqlite3.h"

int main()
{
    WindowInit("Apex System");

    sqlite3* db;
    int rc = sqlite3_open("employee.db", &db);
    if (rc != SQLITE_OK) {
        sqlite3_close(db);
        return -1;
    }


    const char* sql = "CREATE TABLE IF NOT EXISTS employee("
        "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
        "Name TEXT NOT NULL,"
        "Dept TEXT NOT NULL,"
        "Rate REAL NOT NULL,"
        "Salary REAL NOT NULL);";


    while (!WindowShouldClose())
    {
        ScreenUpdate();

        WindowBeginFrame();
        ScreenDraw();
        WindowEndFrame();
    }

    WindowShutdown();
    return 0;
}