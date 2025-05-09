from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
import schedule
from datetime import datetime
#Đề tài tin tức vietnamnet.vn
def thu_thap_tin_tuc():
    trinh_duyet_web = webdriver.Edge()
    trinh_duyet_web.get("https://vietnamnet.vn")
    time.sleep(3.5)


    danh_sach_menu = trinh_duyet_web.find_elements(By.CSS_SELECTOR, "nav a")
    danh_sach_url = [a.get_attribute("href") for a in danh_sach_menu if a.text.strip() and a.get_attribute("href")]

    danh_sach_bai_viet = []

    for duong_dan in danh_sach_url:
        try:
            trinh_duyet_web.get(duong_dan)
            time.sleep(2.5)

            for _ in range(6):
                trinh_duyet_web.execute_script("window.scrollBy(0, 900);")
                time.sleep(1.2)

            trang_html = trinh_duyet_web.page_source
            phan_tich_html = BeautifulSoup(trang_html, "html.parser")
            the_bai_viet = phan_tich_html.select(".horizontalPost__main, .verticalPost__main, .featuredNews__main")

            for tin in the_bai_viet:
                try:
                    tieu_de_html = tin.find("h3", class_=lambda cls: cls and "title" in cls) or tin.find("a", class_=lambda cls: cls and "title" in cls)
                    tieu_de = tieu_de_html.get_text(strip=True)
                except:
                    tieu_de = "Không đọc được"

                try:
                    mo_ta_html = tin.find("div", class_=lambda cls: cls and "desc" in cls) or tin.find("p")
                    mo_ta = mo_ta_html.get_text(strip=True)
                except:
                    mo_ta = "Không rõ"

                try:
                    cha = tin.find_parent("div", class_="horizontalPost") or tin.find_parent("div", class_="verticalPost")
                    the_img = cha.find("img") if cha else tin.find("img")
                    link_anh = the_img.get("data-srcset") or the_img.get("src") or "Không có"
                    link_anh = link_anh.split("?")[0]
                except:
                    link_anh = "Không có"

                danh_sach_bai_viet.append([tieu_de, mo_ta, link_anh])

        except Exception as loi:
            print(f"Lỗi khi tải {duong_dan}: {loi}")

    print(f" Đã ghi nhận {len(danh_sach_bai_viet)} bài viết.")

    bang_ket_qua = pd.DataFrame(danh_sach_bai_viet, columns=["Tiêu đề", "Mô tả", "Hình ảnh"])
    ngay_luu = datetime.now().strftime("%Y-%m-%d")
    ten_tep = f"baiviet_vnn_{ngay_luu}.xlsx"
    bang_ket_qua.to_excel(ten_tep, index=False)

    trinh_duyet_web.quit()



schedule.every().day.at("06:00").do(thu_thap_tin_tuc)
print(" Chờ đến 06:00 để bắt đầu thu thập dữ liệu...")

while True:
    schedule.run_pending()
    time.sleep(60)
