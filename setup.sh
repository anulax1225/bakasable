cd $(dirname "$0")

handle_error() {
    echo "An error occurred on line $1"
    rm -rf ~/.bakasable
    cd $(pwd)
    exit 1
}
trap 'handle_error $LINENO' ERR

echo Installing bakasable
mkdir -m 777 ~/.bakasable
mkdir ~/.bakasable/cache
cp -f ./bin/linux/bakasable ~/.bakasable/

if [ ! $(which premake5) ]; then
    echo Installing premake  
    cp -f ./bin/linux/premake5 ~/.bakasable/
    chmod +x ~/.bakasable/premake5
    echo Installing export-compile-commands module
    cp -rf ./bin/vendor/export-compile-commands ~/.bakasable/
    echo 'require "export-compile-commands"' >> ~/.bakasable/premake-system.lua
fi

echo Searching path in env PATH 
if [ ! $(which bakasable) ]; then
    echo Path not found in env PATH
	echo Adding path
    export PATH=\$PATH:~/.bakasable
    echo "export PATH=\$PATH:~/.bakasable" >> ~/.bashrc
else
    echo Path already added
fi
cd $(pwd)