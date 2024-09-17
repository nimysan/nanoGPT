import time

out_dir = 'out-chinese-poem'
eval_interval = 5
eval_iters = 20
wandb_log = True # feel free to turn on
wandb_project = 'chinese-poem'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'chinese'
init_from = 'resume' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = True
block_size = 256

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1

max_iters = 5300

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False

compile = False # do not torch compile the model