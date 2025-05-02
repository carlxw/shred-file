@echo OFF

set calling_dir=%CD%
set file_arg=%1

pushd %~dp0
python .\shred-file.py %file_arg% %calling_dir%
popd
