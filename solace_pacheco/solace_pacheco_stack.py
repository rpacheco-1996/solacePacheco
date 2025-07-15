from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    Duration,
    aws_iam as iam
)
from constructs import Construct

class SolacePachecoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        openai_layer = _lambda.LayerVersion(
            self,
            "OpenAILayer2",
            code=_lambda.Code.from_asset("openai-layer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="Layer with OpenAI client and dependencies",
        )

        fn = _lambda.Function(
            self,
            "LLMWrapperFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            layers=[openai_layer],
            environment={"HF": "/huggingface"},
            memory_size=256,
            timeout=Duration.seconds(30),
        )

        fn.role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["ssm:GetParameter"],
                resources=[
                    "arn:aws:ssm:us-east-1:<ACCOUNT_ID>:parameter/huggingface" #NOTE: Update this to your own huggingface token parameter
                ],
            )
        )

        apigateway.LambdaRestApi(self, "LLMWrapperAPI", handler=fn)
