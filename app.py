#!/usr/bin/env python3
import os

import aws_cdk as cdk

from solace_pacheco.solace_pacheco_stack import SolacePachecoStack


app = cdk.App()
SolacePachecoStack(app, "SolacePachecoStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
                        region=os.getenv('CDK_DEFAULT_REGION')),
    )

app.synth()
