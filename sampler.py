"""
Defintions for Langevin sampler
"""

import numpy as np

class langevinSampler():
    def __init__(self, beta, grad_potential, n_dim=1):
        """
        Initialize an overdamped Lagevin sampler
        The suggested parameters are beta, the gradient of the potential function and the number of dimensions
        But free feel to modify as needed
        """
        
    def forward_sim_step(self, x0, dt, method="Euler-Maruyama"):
        """
        One-step forward simulation of the SDE
        
        Parameters
        ----------
        x0     : Initial point
        dt     : Time step
        method : "Euler-Maruyama" or "MALA"
        
        Returns
        -------
        x1     : updated state
        """
        
    def sampling(self, x0, dt, num_samples, num_sep, seed, num_burnin=500):
        '''
        Parameters
        ----------
        x0          : Initial point
        dt          : Time step.
        num_samples : Number of samples to generate.
        num_sep     : Number of steps between two consecutive samples
        num_burnin  : Number of burn-in steps

        Returns
        -------
        samples     : Sample vector
        '''