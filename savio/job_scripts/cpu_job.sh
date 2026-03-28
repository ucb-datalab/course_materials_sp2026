#!/bin/bash
# Job name:
#SBATCH --job-name=ay128_cpu_job
#
# Account:
#SBATCH --account=ic_astro128
#
# Quality of Service (QoS):
#SBATCH --qos=savio_normal
#
# Partition:
#SBATCH --partition=savio2_htc
#
# Number of nodes:
#SBATCH --nodes=1
#
# Number of tasks:
#SBATCH --ntasks=1
#
# Processors per task:
#SBATCH --cpus-per-task=1
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

# Activate the course virtual environment managed by uv
source ~/course_materials_sp2026/.venv/bin/activate

# Run your python script
python example_job.py --cpu --num_epochs=1

# Finally run on the cluster using: sbatch cpu_job.sh