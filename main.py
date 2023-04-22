from telethon import TelegramClient, events, sync
import asyncio

api_id = "ele gosta"
api_hash = ''

client=TelegramClient('nu', api_id,api_hash)


async def send_message_after_reply():
    event = asyncio.Event()  
    fff =None

    with open("g.txt", "a+") as file:
        
        
        async def handle_new_message(e):
            r_msg = e.message.message
            

            if "NÃO ENCONTRADO!" in r_msg:
                
                await client.send_message(' ', f"/  1 {fff}")

                
                print("reenviando")

            else:
                print(f"registrado: {fff}")
                file.write(r_msg)
            event.set()
            

        client.add_event_handler(handle_new_message, events.NewMessage(chats=' ', incoming=True))

        await client.start()

        with open("c.txt", "r") as f:
            
            lines = f.readlines()
            for i in range(len(lines)):
                fff = lines[i].split("|")[0]
                print(f"Na linha: {i}")
                await client.send_message(' ', f"/  2 {fff}")
              
                try:
                    await asyncio.wait_for(event.wait(), timeout=30.0)
                except asyncio.TimeoutError:
                    print("Timeout, reenviando mensagem...")
                    await client.send_message(' ', "Rsrs")

                    await client.send_message(' ', f"/  3 {fff}")

                    continue
               

                event.clear()  

loop = asyncio.get_event_loop()
loop.run_until_complete(send_message_after_reply())
