# 🤖 Forward Tag Remover Bot

এটি একটি শক্তিশালী টেলিগ্রাম বট যা ফরোয়ার্ড করা মেসেজ থেকে "Forwarded from" ট্যাগ রিমুভ করে নতুন করে মেসেজ সেন্ড করে।

**Developed by:** [Ahad islam](https://t.me/Sofikul46)  
**Updates Channel:** [Tricks and Earn 2](https://t.me/TricksandEarn2)

---

## 🌟 ফিচারসমূহ
✅ মেসেজ থেকে ফরোয়ার্ড ট্যাগ রিমুভ করে।
✅ ছবি, ভিডিও এবং ফাইল সাপোর্ট করে।
✅ চ্যানেল এবং গ্রুপে কাজ করে।
✅ সহজ সেটআপ এবং ডিপ্লয়মেন্ট।

---

## ⚙️ কনফিগারেশন (Environment Variables)
বটটি রান করার জন্য নিচের ভেরিয়েবলগুলো সেট করুন:

| ভেরিয়েবল | বিবরণ |
| :--- | :--- |
| `8464668732:AAHiSWZCpd5Eao_507QEUgwBx0MXYmLRtOA` | বটের টোকেন [@BotFather](https://t.me/BotFather) থেকে নিন |
| `25369886` | [my.telegram.org](https://my.telegram.org) থেকে নিন |
| `6a497a2a672acf2daa2b2c57e84157df` | [my.telegram.org](https://my.telegram.org) থেকে নিন |
| `7720580351` | আপনার টেলিগ্রাম ইউজার ID ( [@userinfobot](https://t.me/userinfobot) ) |

---

## 🚀 ডিপ্লয়মেন্ট মেথড

### ☁️ One-Click Deployment (সহজ পদ্ধতি)
সরাসরি ক্লাউড সার্ভারে আপলোড করতে নিচের বাটনে ক্লিক করুন:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/Ahad736/Forward-Tag-Remover-My)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Ahad736/Forward-Tag-Remover-My)

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/services/deploy?name=forward-tag-remover&repository=Ahad736/Forward-Tag-Remover-My&branch=main&type=git&env[TOKEN]=REPLACE_ME&env[OWNER]=REPLACE_ME&env[API_HASH]=REPLACE_ME&env[API_ID]=REPLACE_ME)

### 🐧 Ubuntu / Local Deployment
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/Ahad736/Forward-Tag-Remover-My
cd Forward-Tag-Remover-My
pip3 install -r requirements.txt
python3 bot.py