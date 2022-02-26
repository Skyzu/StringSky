from pyrogram.types import InlineKeyboardButton
import random

class Data:
    #start Pic
  photo=random.choice(ALL_PIC), 
    ALL_PIC = [
 "https://te.legra.ph/file/28f95b221efbefede9988.jpg", 
 "https://telegra.ph/file/290e055a47df326b6e908.jpg", 
 "https://telegra.ph/file/4a2c348dc10f4799ecc23.jpg", 
 "https://telegra.ph/file/e5d14734cc62fb45ebb80.jpg", 
 "https://telegra.ph/file/52771fab9aa447154ecfd.jpg", 
 "https://telegra.ph/file/28af6e4d2f6c9849ccd8e.jpg", 
 "https://telegra.ph/file/de94973a185e70e207363.jpg", 
 "https://telegra.ph/file/c2ff65c5f7ddbb6a52170.jpg"
]

    # Start Message
    START = """
Halo {}

Selamat datang {}

Jika kamu tidak percaya bot ini, 
1) gausah baca pesan ini
2) blokir bot atau delete chat

Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih
By @skyzu
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ​", url="https://t.me/skyzu")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ​​", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴꜰᴏ ʙᴏᴛ ʟᴀɪɴɴʏᴀ​", url="https://t.me/ProjectSkyzu")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @SkyStringBot

Group Support : [Gabung](https://t.me/skyzusupport)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @skyzu
    """
