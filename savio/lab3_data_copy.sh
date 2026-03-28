# 1. Create a data directory in your home folder and navigate into it
mkdir -p ~/galaxyzoo_data
cd ~/galaxyzoo_data

# 2. Copy the files from the shared project space
cp /global/home/groups/ic_astro128/lab3/data/training_classifications.csv .
cp /global/home/groups/ic_astro128/lab3/data/training_images.tar .
cp /global/home/groups/ic_astro128/lab3/data/test_images.tar .

# 3. Extract the image directories
tar -xf training_images.tar
tar -xf test_images.tar