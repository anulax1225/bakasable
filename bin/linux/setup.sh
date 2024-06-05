echo Installing bakasable
handle_error() {
    echo "An error occurred on line $1"
    rm -rf ~/.bakasable
    exit 1
}
trap 'handle_error $LINENO' ERR
mkdir -m 777 ~/.bakasable
mkdir ~/.bakasable/cache
cp ./bakasable ~/.bakasable/
echo "export PATH=$PATH:~/.bakasable" >> ~/.bashrc
