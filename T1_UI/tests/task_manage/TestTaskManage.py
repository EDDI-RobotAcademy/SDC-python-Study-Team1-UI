import unittest
from unittest import mock

from task_manage.entity.TaskEntity import TaskEntity
from task_manage.repository.TaskManageRepositoryImpl import TaskManageRepositoryImpl
from task_manage.service.TaskManageServiceImpl import TaskManageServiceImpl


class TestTaskManage(unittest.TestCase):
    def testTaskManageGetInstance(self):
        print(f'TaskManage Instance 가져오고싶어')

        # taskManageRepository = TaskManageRepositoryImpl()
        # 위에꺼가 있다고 가정하고 작성하면 아래와 같음
        # mock 은 혁명이다
        taskManageService = TaskManageServiceImpl(mock)

    def testTaskEntity(self):
        print(f'Taskentity')
        taskPid = 123
        target = 'dffd'
        args = 7895

        task_entity_instance = TaskEntity(taskPid, target, args)


        print("TaskPid:", task_entity_instance.getTaskPid())
        print("Target Function:", task_entity_instance.getTarget())
        print("Arguments:", task_entity_instance.getArgs())


if __name__ == '__main__':
    unittest.main()