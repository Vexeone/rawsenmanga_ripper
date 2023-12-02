import os
import requests

def download_images(title, chapter_number, end_page):
    base_url = "https://raw.senmanga.com/viewer/{}/{}/{}"
    output_folder = os.path.join("downloads", title, f"Chapter{chapter_number}")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_number in range(1, end_page + 1):
        url = base_url.format(title, chapter_number, page_number)
        response = requests.get(url)

        if response.status_code == 200:
            image_name = f"{page_number}.jpg"
            image_path = os.path.join(output_folder, image_name)

            with open(image_path, 'wb') as file:
                file.write(response.content)

            print(f"Done: {page_number}/{end_page}")
        else:
            print(f"4to to poshlo po pizde na str {page_number}. status code: {response.status_code}")
            break

if __name__ == "__main__":
    title = input("title name(from url): ")
    chapter_number = int(input("chapter number: "))
    end_page = int(input("last page number: "))

    download_images(title, chapter_number, end_page)
