# **Генерация одежды по текстовому описанию**

## **Описание проекта**

В рамках данного проекта будет реализован сервис генерации одежды по текстовому описанию с помощью Stable Diffusion, в том числе с добавлением на основании пользовательских изображений (DreamBooth, LoRA).

## **Команда**

- **Синецкий Андрей**
  
Куратор: **Макарова Мария**

## **План работы**

1. Сбор данных
   - Выбор базовой модели
   - Сбор изображений для обучения
2. Настройка пайплайна генерации и обучения моделей
   - Генерация изображений по описанию при помощи Stable Diffusion
   - Обучение модели: DreamBooth, LoRA
   - Генерация одежды на белом фоне, в продуктовом формате
3. Продуктивизация сервиса: Telegram-бот


## **Итоги работы**

* Произведена выборка 45 фотографий футболок в классическом продуктовом виде на белом фоне. Датасет для этого проекта можно скачать [здесь](https://disk.yandex.ru/d/9AbJz3lHwdbpHg)
* Выбрана [модель](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors) SDXL 1.0 в качестве базовой 
* Изображения из дата-сета были отредактированы в Photoshop до размера 1024x1024, необходимого для обучения модели
![6tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/9a1bd392-3146-47db-8f50-fedf1ca08441)
![5tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/4c8cc689-0521-4aa1-ba65-ed57baa179a9)
![4tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/17d0e7b2-99ba-4719-a63d-9775a23daeea)
![3tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/19f96964-fbe4-4265-bf56-f34b704f5de3)
![2tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/8b20c884-3fd7-43ed-9a23-a0c49e884fd7)
![1tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/cd2c901b-46e7-4257-91d8-e5edf85e318a)
![13tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/a05cff59-b3fc-4795-9896-fbc47944be94)
![12tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/ca713ed8-7e16-4238-92e0-e03a590a9016)
![11tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/702103fb-2da6-4adc-9642-d885dc6435c4)
![10tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/decec336-7ec0-4764-bfb8-358b8b0982c6)
![9tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/19147b4b-5cbe-46aa-bc63-1b479f4bdb8b)
![8tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/4bb8dd64-d32d-4389-88ea-a50e2a59e5c9)
![7tshclthss](https://github.com/Soltechml/ClothesLora/assets/146172822/ed2c5e37-a425-4313-938f-270e1b1926a3)




* Была обучена модель LoRA на основе SDXL 1.0 в Google Colab
* Произведено тестирование обученной модели в интерфейсе ComfyUI

