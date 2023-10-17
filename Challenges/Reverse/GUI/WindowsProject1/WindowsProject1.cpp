
#include <Windows.h>
#include <string>

HWND g_hWnd;

std::wstring EncryptFlag(const std::wstring& input) {
    std::wstring encrypted;
    for (wchar_t c : input) {
        wchar_t encryptedChar = (c - 5) ^ 0x51;  // 加一操作
        encrypted += encryptedChar;
    }
    return encrypted;
}

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam) {
    switch (message) {
    case WM_CREATE:
        CreateWindow(TEXT("STATIC"), TEXT("Please input flag:"),
            WS_CHILD | WS_VISIBLE,
            10, 10, 120, 20,
            hWnd, NULL, NULL, NULL);

        CreateWindow(TEXT("EDIT"), TEXT(""),
            WS_CHILD | WS_VISIBLE | WS_BORDER,
            10, 40, 250, 30,
            hWnd, (HMENU)2, NULL, NULL);

        CreateWindow(TEXT("BUTTON"), TEXT("submit"),
            WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            10, 80, 80, 30,
            hWnd, (HMENU)1, NULL, NULL);
        break;

    case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hWnd, &ps);

        // 绘制窗口背景颜色为白色
        HBRUSH hBrush = CreateSolidBrush(RGB(255, 255, 255));
        FillRect(hdc, &ps.rcPaint, hBrush);
        DeleteObject(hBrush);

        EndPaint(hWnd, &ps);
    }
    break;

    case WM_COMMAND:
        switch (LOWORD(wParam)) {
        case 1:
            TCHAR buffer[512];
            GetWindowText(GetDlgItem(hWnd, 2), buffer, sizeof(buffer));
            std::wstring input = buffer;

            // 对输入进行加密操作
            std::wstring encryptedInput = EncryptFlag(input);

            // 正确加密后的 flag
            std::wstring correctEncryptedFlag = L"\x39\x3b\x31\xf\x3e\x30\x27\x13\x1\x7d\x70\x70\x3\x7d\x38\xe\x7a\x23\x7c\xb\x1a\x3c\x7d\x39\x7f\x3c\x4d\x4d\x4d\x29";

            if (encryptedInput == correctEncryptedFlag) {
                MessageBox(hWnd, TEXT("Congratulations! flag is correct！"), TEXT("hint"), MB_OK);
            }
            else {
                MessageBox(hWnd, TEXT("Sorry, flag error."), TEXT("hint"), MB_OK);
            }
            break;
        }
        break;

    case WM_CLOSE:
        DestroyWindow(hWnd);
        break;

    case WM_DESTROY:
        PostQuitMessage(0);
        break;

    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    WNDCLASS wc = { 0 };
    wc.lpfnWndProc = WndProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = TEXT("FlagCheckerWindowClass");
    RegisterClass(&wc);

    g_hWnd = CreateWindow(TEXT("FlagCheckerWindowClass"), TEXT("Windows Flag Checker"),
        WS_OVERLAPPEDWINDOW,
        100, 100, 300, 200,
        NULL, NULL, hInstance, NULL);

    ShowWindow(g_hWnd, nCmdShow);
    UpdateWindow(g_hWnd);
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return (int)msg.wParam;
}




