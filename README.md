# Ashs PDF Manipulator

## Because sometimes you just need to make PDFs your bitch without paying Adobe £29.99 a month for the privilege.




Built with PyQt5, pypdf, and the kind of dark-blue colour palette that whispers “Yeah.......yeah I'm OG.”

## What This Spicy Little Program Does
### Merge PDFs

<img width="901" height="658" alt="image" src="https://github.com/user-attachments/assets/a082c37e-a726-47eb-a3db-b80fb178af73" />

- Pick up to six PDFs (combine over multiple runs for infinite PDF Addition!)

- **Give the resulting monstrosity a browser tab name so Chrome stops calling it final_final_rev3_REAL.pdf**

- Click MERGE

- Boom. New PDF. You are now the god of documents.

### Split PDFs 
<img width="897" height="656" alt="image" src="https://github.com/user-attachments/assets/487b1c51-f75a-465c-8998-ddd0dfc9f688" />


- Load a PDF

- Choose a page to slice at

**The app creates:**

- First PDF: pages 1 → split-1

- Second PDF: pages split → end

- Name them something sensible… or something petty, depending on mood

- Optional: give each child-PDF its own browser tab name (identity is important)

- Save them wherever your desktop chaos pile lives

## Requirements

**Install these or perish:**

pip install -r requirements.txt

### That’s it.
#### No arcane rituals, no Java, no 17GB of Adobe updates.


## Folder Structure (in case you actually care)
Ashs_PDF_Manipulator/
│  
├── main.py  
├── modules/  
│   ├── gui.py  
│   ├── pdf_utils.py  
│   └── theme.py  
├── requirements.txt  
├── pepePDFPNG.png (PNG to build the .ico out of)  
├── pepeico.ico (actual .ico for the build)  
├── build_cmd.txt (build command for pyinstaller)  
├── requirements.txt  
└── README.md  



**It’s organised.
Unlike your Downloads folder.**

## How to Just Run This Thing

There's now an exe release!! Download and go nuts!

## How to Run This Thing From Source if You're OG

From the project folder:

python main.py


A window will appear.
If it doesn’t, sacrifice a USB cable to the computing gods and try again.

## Highlights (aka “Why this app slaps”)

- Custom browser tab titles, because vibes matter

- No subscriptions, no DRM, no Adobe snitching on you

- My signature glowing dark theme (because light colour schemes make me envy the blind) 

- Works locally, offline, and without phoning home to Adobe

## Why This Exists

- Because Adobe thinks clicking one button should cost as much as a gym membership.

- Because you deal with PDFs daily and deserve a tool that doesn’t scream at you.

- Because you could build this yourself… but why bother, it's here!

## Future Features (maybe)


- Rotate pages. Right round....Like a like a record baby (right round *)

- Auto-rename PDFs based on pure spite

- A button that simply says “FUCK THIS PDF” and outputs a JPEG Goatse instead

- A feature that screams when someone uploads a Word document saved **_as_** a PDF

- *(Round round)
- ~~Legit i will make this an executable when I have the willpower~~ **DONE**

## License

**Use it, abuse it, redistribute it, tattoo it on your face — whatever.
If it breaks, you get to keep both halves.**

### PS. Fuck Adobe

