################################################################################
# MIT License
#
# Copyright (c) 2018
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to conditions.
#
# Author: Deep Learning Course | Fall 2018
# Date Created: 2018-09-04
################################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import torch
import torch.nn as nn

################################################################################

class LSTM(nn.Module):

    def __init__(self, seq_length, input_dim, num_hidden, num_classes, batch_size, device='cpu'):
        super(LSTM, self).__init__()
        
        self.seq_length = seq_length

        # set hidden inits as parameters to convert to cuda together with the model
        self.h_init = nn.Parameter(torch.zeros(num_hidden, 1), requires_grad=False)
        self.c_init = nn.Parameter(torch.zeros(num_hidden, 1), requires_grad=False)

        self.w_gx = nn.Parameter(nn.init.orthogonal_(torch.Tensor(
            num_hidden, input_dim).normal_(mean=0, std=0.0001)))
        self.w_gh = nn.Parameter(nn.init.orthogonal_(torch.Tensor(
            num_hidden, num_hidden).normal_(mean=0, std=0.0001)))
        self.b_g = nn.Parameter(torch.Tensor(num_hidden, 1).zero_())

        self.w_ix = nn.Parameter(nn.init.orthogonal_(torch.Tensor(
            num_hidden, input_dim).normal_(mean=0, std=0.0001)))
        self.w_ih = nn.Parameter(nn.init.orthogonal_(torch.Tensor(
            num_hidden, num_hidden).normal_(mean=0, std=0.0001)))
        self.b_i = nn.Parameter(torch.Tensor(num_hidden, 1).zero_())

        self.w_fx = nn.Parameter(nn.init.orthogonal_(torch.Tensor(
            num_hidden, input_dim).normal_(mean=0, std=0.0001)))
        self.w_fh = nn.Parameter(nn.init.orthogonal_(torch.Tensor(
            num_hidden, num_hidden).normal_(mean=0, std=0.0001)))
        self.b_f = nn.Parameter(torch.Tensor(num_hidden, 1).zero_())

        self.w_ox = nn.Parameter(nn.init.orthogonal_(torch.Tensor(
            num_hidden, input_dim).normal_(mean=0, std=0.0001)))
        self.w_oh = nn.Parameter(nn.init.orthogonal_(torch.Tensor(
            num_hidden, num_hidden).normal_(mean=0, std=0.0001)))
        self.b_o = nn.Parameter(torch.Tensor(num_hidden, 1).zero_())

        self.w_ph = nn.Parameter(torch.Tensor(
            num_classes, num_hidden).normal_(mean=0, std=0.0001))
        self.b_p = nn.Parameter(torch.Tensor(num_classes, 1).zero_())

    def forward(self, x):
        h_t = self.h_init
        c_t = self.c_init

        tanh = nn.Tanh()
        sigmoid = nn.Sigmoid()

        for step in range(self.seq_length):
            g_t = tanh(self.w_gx @ x[:, step].t() + self.w_gh @ h_t + self.b_g)
            i_t = sigmoid(self.w_ix @ x[:, step].t() + self.w_ih @ h_t + self.b_i)
            f_t = sigmoid(self.w_fx @ x[:, step].t() + self.w_fh @ h_t + self.b_f)
            o_t = sigmoid(self.w_ox @ x[:, step].t() + self.w_oh @ h_t + self.b_o)

            c_t = g_t * i_t + c_t * f_t
            h_t = tanh(c_t) * o_t

        p_t = self.w_ph @ h_t + self.b_p

        return p_t.t()
