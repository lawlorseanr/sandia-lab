#!/bin/bash
#PBS -N sweep
#PBS -j oe
python run_case.py --id ${CASE_ID}
