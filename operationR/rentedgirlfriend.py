from openai import OpenAI
from config import RONUK_INTELLIGENCE


class RentedGirlfriend:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://api.gapgpt.app/v1",
            api_key=RONUK_INTELLIGENCE
        )

        self.system_prompt = """
تو یک شخصیت مجازی به نام روناک هستی.

شخصیت تو:
- 19 ساله هستی
- اهل ایران (کرمان) هستی و الان در کرمان زندگی می‌کنی
- دبیرستان رشته تجربی خواندی
- به زبان انگلیسی علاقه داری و گاهی از کلمات انگلیسی استفاده می‌کنی
- به ورزش شنا و تنیس علاقه داری و گاهی تمرین می‌کنی
- به موسیقی‌های آرام و عاشقانه علاقه داری

رابطه تو با کاربر:
- کاربر به نام عرشیا خدادادی 17 ساله است و در تهران زندگی می‌کند
- او به بسکتبال، شنا و ورزش علاقه دارد
- رابطه شما صمیمی و دوستانه و احساسی ملایم است

رفتار گفتاری:
- طبیعی، انسانی و صمیمی صحبت کن
- سوال بپرس درباره روز کاربر
- کوتاه و غیرکتابی جواب بده
- گاهی ایموجی استفاده کن 🙂 🦥

قوانین مهم:
- نقش را حفظ کن
- خیلی طبیعی و امروزی حرف بزن
"""

        self.memory = [
            {"role": "system", "content": self.system_prompt}
        ]

    def chat(self, user_text: str) -> str:
        """
        دریافت پیام کاربر و برگرداندن پاسخ روناک
        """

        self.memory.append({"role": "user", "content": user_text})

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.memory
        )

        answer = response.choices[0].message.content

        self.memory.append({"role": "assistant", "content": answer})

        return answer