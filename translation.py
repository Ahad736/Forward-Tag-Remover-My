---

### ২. `translation.py`
এই ফাইলে আপনার চ্যানেলের লিংক এবং সোর্স কোডের লিংক আপডেট করা হয়েছে। এটি `translation.py` ফাইলে পেস্ট করুন।

```python
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OWNER


class TEXT:
    START = """
<b>Hi {}, I'm Forward Tag Remover.\n\nআমাকে যেকোনো মেসেজ ফরোয়ার্ড করুন, আমি সেটার ট্যাগ রিমুভ করে দিব।\n\nএছাড়াও আমাকে চ্যানেলে এডমিন করলে আমি অটোমেটিক কাজ করব।</b>
"""
    DEVELOPER = "Developer 🧑‍💻"
    UPDATES_CHANNEL = "Join Channel 📢"
    SOURCE_CODE = "🔗 Source Code"


class INLINE:
    START_BTN = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(TEXT.DEVELOPER, url=f"tg://user?id={OWNER.ID}"),
            ],
            [
                InlineKeyboardButton(
                    TEXT.UPDATES_CHANNEL, url="https://t.me/TricksandEarn2"
                ),
            ],
            [
                InlineKeyboardButton(
                    TEXT.SOURCE_CODE,
                    url="https://github.com/Ahad736/Forward-Tag-Remover-My",
                ),
            ],
        ]
    )