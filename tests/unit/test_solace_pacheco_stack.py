import aws_cdk as core
import aws_cdk.assertions as assertions

from solace_pacheco.solace_pacheco_stack import SolacePachecoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in solace_pacheco/solace_pacheco_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SolacePachecoStack(app, "solace-pacheco")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
