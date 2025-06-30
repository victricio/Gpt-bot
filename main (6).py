import telegram
import asyncio

TELEGRAM_BOT_TOKEN = '8170132422:AAH-lSJwWCWDRe9Usr_LnrEksnpu58xPa0c'
USER_ID = 7814084863

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

async def enviar_senal(mensaje):
    try:
        await bot.send_message(chat_id=USER_ID, text=mensaje)
        print("✅ Señal enviada correctamente")
    except Exception as e:
        print(f"❌ Error al enviar señal: {e}")

if __name__ == '__main__':
    mensaje = "🚨 Nueva señal: EUR/USD posible entrada a la baja con cruce de EMA 9 y 21."
    asyncio.run(enviar_senal(mensaje))
