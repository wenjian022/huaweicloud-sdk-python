# -*-coding:utf-8 -*-

from openstack import connection

# create connection
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


def get_quotas():
    quota = conn.ecs.quotas()
    print (quota)
    print (quota.maxsecuritygrouprules)


if __name__ == "__main__":
    get_quotas()

