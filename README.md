# PDF to TXT

Extract text from PDF files with OCR

## Usage

### With container

```bash
bash ./build.sh
bash ./run <input_folder> <output_folder>
```

### Local

```bash
pip install -r requirements.txt
python lib/main.py -i <input_folder> <output_folder>
```

## Test

### With container

```bash
bash ./build.sh
bash ./run.sh ./test/input ./test/output
```

### Local

```bash
python lib/main.py -i ./test/input -o ./test/output
```