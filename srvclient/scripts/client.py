#!/usr/bin/python3
#author: muks
import rospy
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse

class client:
	def __init__(self, srv_name):
		rospy.init_node("client_node")
		rospy.wait_for_service(srv_name)

		try:
			self.client=rospy.ServiceProxy(srv_name, SetBool)
			request=SetBoolRequest()
			request.data=True
			print("Send Request: ", request)
			response=self.client(request)
			print("Got Response: ", response)

		except rospy.ServiceException as e:
			print("service call failed %s"%e)

if __name__=='__main__':
		c=client("boolcall")
		