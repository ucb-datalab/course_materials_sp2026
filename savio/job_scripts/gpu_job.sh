# Job name:
#SBATCH --job-name=example_gpu_job
#
# Account:
#SBATCH --account=ic_astro128
#
# Partition:
#SBATCH --partition=savio2_1080ti
#
# Number of nodes:
#SBATCH --nodes=1
#
# Number of tasks (one for each GPU desired for use case):
#SBATCH --ntasks=1
#
# Processors per task:
#SBATCH --cpus-per-task=2
#
#Number of GPUs
#SBATCH --gres=gpu:1
#
# Wall clock limit:
#SBATCH --time=00:20:00
#
#SBATCH --output=test_job_%j.out
#SBATCH --error=test_job_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=smogan@berkeley.edu

module load python
module load ml/pytorch
module load cuda

# Activate the course virtual environment managed by uv
# Be sure to replace the env below with the path you have chosen
source ~/course_materials_sp2026/.venv/bin/activate

# Run your python script
python example_job.py --gpu --num_epochs=10

# Finally run on the cluster using: sbatch gpu_job.sh