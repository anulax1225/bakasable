echo "Searching path in env PATH"
$PATH = [Environment]::GetEnvironmentVariable("PATH", "Machine")
$bakasable_path = "C:\Program Files\bakasable"
if( $PATH -notlike "*"+$bakasable_path+"*" ){
	echo "Path not found in env PATH"
	echo "Adding path"
    	[Environment]::SetEnvironmentVariable("PATH", "$PATH;$bakasable_path", "Machine")
}
else {
	echo "Path already added"
}