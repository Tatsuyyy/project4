from graphene_django.types import DjangoObjectType
import graphene
from graphene import Mutation, ObjectType
from earap.models import Actions, Projects, Steps
from earap.scraping.DriverClass import Driver
from earap.scraping.StepClass import Step


class StepsType(DjangoObjectType):
    class Meta:
        model = Steps

class StepMutation(Mutation):
    class Arguments:
        num = graphene.Int(required=True)
        xpath = graphene.String(required=True)
        value = graphene.String(required=True)
        action_id = graphene.ID(required=True)
        elem_id = graphene.ID(required=True)
        project_id = graphene.ID(required=True)

    step = graphene.Field(StepsType)

    def mutate(self, info, num, xpath, value, action_id, elem_id, project_id):
        # action = Actions.objects.get(id=action_id)
        # elem = Elems.objects.get(id=elem_id)
        # project = Projects.object.get(id=project_id)
        step = Steps.objects.create(order_num=num, xpath=xpath, value=value, action=action_id, elem=elem_id, project_id=project_id)
        step.save()
        return StepMutation(step=step)


class Mutation(ObjectType):
    create_step = StepMutation.Field()

class ActionsType(DjangoObjectType):
    class Meta:
        model = Actions
class ProjectsType(DjangoObjectType):
    class Meta:
        model = Projects
class Query(object):
    all_steps = graphene.List(StepsType)
    all_actions = graphene.List(ActionsType)
    all_projects = graphene.List(ProjectsType)
    project = graphene.Field(ProjectsType, id=graphene.Int())

    def resolve_all_steps(self, info):
        return Steps.objects.all()

    def resolve_all_actions(self, info):
        return Actions.objects.all()

    def resolve_all_projects(self, info):
        return Projects.objects.all()

    def resolve_project(self, info, id):
        prj = Projects.objects.filter(pk=id).first()
        driver = Driver(prj.url)
        steps = Steps.objects.filter(project_id=prj.id)
        xpath: Step = [{'num': step.order_num, 'xpath': step.xpath, 'action': step.action.name, 'value': step.value} for step in steps]
        driver.chain_steps(xpath)
        return Projects.objects.filter(pk=id).first()



