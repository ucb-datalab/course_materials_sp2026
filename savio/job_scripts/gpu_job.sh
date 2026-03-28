#!/bin/bash
# Job name:
#SBATCH --job-name=ay128_gpu_job
#
# Account:
#SBATCH --account=ic_astro128
#
# Quality of Service (QoS):
#SBATCH --qos=savio_normal
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
# Always at least twice the number of GPUs
#SBATCH --cpus-per-task=2
#
# Number of GPUs:
#SBATCH --gres=gpu:1
#
# Wall clock limit:
#SBATCH --time=00:10:00
#
# Job Output/Error files:
#SBATCH --output=test_job_%j.out
#SBATCH --error=test_job_%j.err
#
# Email notifications:
#SBATCH --mail-type=ALL
#SBATCH --mail-user=your_email@berkeley.edu

module load cuda

# Activate the course virtual environment managed by uv
source ~/course_materials_sp2026/.venv/bin/activate

# Run your python script
python example_job.py --gpu --num_epochs=10

# Finally run on the cluster using: sbatch gpu_job.sh