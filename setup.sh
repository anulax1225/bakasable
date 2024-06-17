echo Installing bakasable

cd $(dirname "$0")

handle_error() {
    echo "An error occurred on line $1"
    rm -rf ~/.bakasable
    cd $(pwd)
    exit 1
}
trap 'handle_error $LINENO' ERR

mkdir -m 777 ~/.bakasable
mkdir ~/.bakasable/cache

cp -f ./bin/linux/bakasable ~/.bakasable/
if [ ! $(which premake5) ]; then
    cp -f ./bin/linux/premake5 ~/.bakasable/
fi

echo Searching path in env PATH 
if [ ! $(which bakasable) ]; then
    echo Path not found in env PATH
	echo Adding path
    echo "export PATH=\$PATH:~/.bakasable" >> ~/.bashrc
else
    echo Path already added
fi
cd $(pwd)