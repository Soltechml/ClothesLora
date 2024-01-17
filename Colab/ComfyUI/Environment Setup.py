#@title Environment Setup

from pathlib import Path

OPTIONS = {}

USE_GOOGLE_DRIVE = True  #@param {type:"boolean"}
UPDATE_COMFY_UI = False  #@param {type:"boolean"}
WORKSPACE = 'ComfyUI'
OPTIONS['USE_GOOGLE_DRIVE'] = USE_GOOGLE_DRIVE
OPTIONS['UPDATE_COMFY_UI'] = UPDATE_COMFY_UI

if OPTIONS['USE_GOOGLE_DRIVE']:
    !echo "Mounting Google Drive..."
    %cd /
    
    from google.colab import drive
    drive.mount('/content/drive')

    WORKSPACE = "/content/drive/MyDrive/ComfyUI"
    %cd /content/drive/MyDrive

![ ! -d $WORKSPACE ] && echo -= Initial setup ComfyUI =- && git clone https://github.com/comfyanonymous/ComfyUI
%cd $WORKSPACE

if OPTIONS['UPDATE_COMFY_UI']:
  !echo -= Updating ComfyUI =-
  !git pull

!echo -= Install dependencies =-
!pip install xformers!=0.0.18 -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu121 --extra-index-url https://download.pytorch.org/whl/cu118 --extra-index-url https://download.pytorch.org/whl/cu117
