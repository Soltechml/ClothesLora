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
* Была обучена модель LoRA на основе SDXL 1.0 в Google Colab
* Произведено тестирование обученной модели в интерфейсе ComfyUI

![photo_5276295589048475807_y](https://github.com/Soltechml/ClothesLora/assets/146172822/c5aeb155-e9da-4d30-90c9-9692fa8c004b)


