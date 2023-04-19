from telethon import TelegramClient, events, sync
import asyncio

api_id = 222222222
api_hash = 'aiaiaiai'

client=TelegramClient('aaa', api_id,api_hash)



async def send_message_after_reply():
    event = asyncio.Event()  # Cria um evento asyncio

    with open("output.txt", "a+") as file:
        async def handle_new_message(e):
            r_msg = e.message.message

            if "PARAM: XX" in r_msg:
                file.write(r_msg)
                print("registrado")
            else:
                print("Nao registrado")
            event.set()

        client.add_event_handler(handle_new_message, events.NewMessage(chats='Nomedochat'))

        await client.start()

        with open("input.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                fff = line.split("|")[0]
                await client.send_message('Nomedochat', f"/telegramparam {fff}")
                try:
                    await asyncio.wait_for(event.wait(), timeout=10.0)
                except asyncio.TimeoutError:
                    print("Timeout, reenviando mensagem...")
                    continue
                event.clear()  

loop = asyncio.get_event_loop()
loop.run_until_complete(send_message_after_reply())
