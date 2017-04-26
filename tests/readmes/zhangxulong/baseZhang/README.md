# A python module for audio and music processing

# baseZhang
[![baseZhang](https://img.shields.io/pypi/v/baseZhang.svg)](https://pypi.python.org/pypi/baseZhang)
[![baseZhang](https://img.shields.io/pypi/dm/baseZhang.svg "PyPi Downloads")](https://pypi.python.org/pypi/baseZhang)


## INFO
function list:

```python
from .baseZhang import align_two_list_with_same_len, del_the_file, if_no_create_it, init_data_dir, print_to_check, \
savefig, update_pip_install_packages, wavread, wavwrite
from .calcChroma import calcChroma
from .calcMFCC import calcMFCC, calcMFCC_delta, calcMFCC_delta_delta, fbank, log_fbank, log_spectrum_power
from .callMatlabFunction import run_matlab_codes
from .countDays import countDaysBettweenTwo
from .datasetPreprocess import class_encoder_to_number, class_number_encode_to_one_hot_code, \
one_hot_code_to_class_number_encode, number_to_class_name, split_dataset_to_tain_test, load_train_test_data
from .formatTrans import mp32Wav, mpeg2wav, wav2MFCC, video2mp4
from .modifyMarkdown import modify_markdown
from .plotVisualData import plot_waveform, plotDuralWav, plotmono_waveform, plotstereo_waveform, plotstft, plotMonoWav, \
plotssd, plotmatrix
from .recordAudio import recordAudio
from .split2word import split_into_words
from .videoProcess import videoProcess
from .youtubeDownload import download_youtube, download_youtube_playlist, pdf_link_2_txt, rename_tag
```

# @windows

1. choose python 2.7.13 and pls use the X86 not the X86-X64 installer package.
2. install scipy by the 32bit installer package of exe.
3. change backend from tensorflow to theano
    search your file system and find the keras.json file. change the contends from tensorflow to theano.
4. download and install ffmpeg from ffmpeg.org
5. use pip install baseZhang

# install_requires

['numpy==1.12.1', 'pandas==0.19.2', 'matplotlib==2.0.0', 'h5py==2.7.0', 'tqdm==4.11.2',
                      'PyAudio==0.2.11', 'pydub==0.18.0', 'pyPdf==1.13', 'PyYAML==3.12', 'six==1.10.0',
                      'SoundFile==0.9.0.post1', 'Theano==0.9.0', 'scikit-learn==0.18.1', 'Keras==1.2.2'],
 