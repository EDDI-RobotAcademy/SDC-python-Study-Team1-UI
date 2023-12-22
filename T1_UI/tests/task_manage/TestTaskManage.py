import unittest
from unittest import mock

from task_manage.repository.TaskManageRepositoryImpl import TaskManageRepositoryImpl
from task_manage.service.TaskManageServiceImpl import TaskManageServiceImpl


class TestTaskManage(unittest.TestCase):
    def testTaskManageGetInstance(self):
        print(f'TaskManage Instance 가져오고싶어')

        # taskManageRepository = TaskManageRepositoryImpl()
        # 위에꺼가 있다고 가정하고 작성하면 아래와 같음
        # mock 은 혁명이다
        taskManageService = TaskManageServiceImpl(mock)


if __name__ == '__main__':
    unittest.main()