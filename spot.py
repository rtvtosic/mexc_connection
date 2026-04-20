import websocket
import json


MEXC_URL = "wss://contract.mexc.com/edge"
FILENAME = "data"

def on_message(ws, message) -> str:
    """Вызывается, когда приходят данные с биржи"""
    print(f"Получено сообщение: {message}")
    with open(f'{FILENAME}.json', 'a') as file:
        file.write(message + '\n')
        print(f"В файл {FILENAME}.json добавлены данные")
    
    print("========================")

def on_open(ws):
    """Вызывается сразу после подключения"""
    print("=== CONNECTED ===")

    # Формирование подписки
    subscription_msg = {
        "method": "sub.ticker",
        "param": {
            "symbol": "BTC_USDT"
        }
    }

    # Отправка запроса на подписку в формате json
    ws.send(json.dumps(subscription_msg))
    print("Запрос на подписку успешно отправлен")

if __name__ == "__main__":
    ws_app = websocket.WebSocketApp(
        MEXC_URL,
        on_open=on_open,
        on_message=on_message
    )

    ws_app.run_forever()

