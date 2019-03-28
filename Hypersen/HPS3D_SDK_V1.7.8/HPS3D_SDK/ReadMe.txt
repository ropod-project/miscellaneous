*******************************************************************************
Readme HPS_3DTOF HPS3D_SDK v1.7.8

Hypersen Technologies Copyright ©  2019                  Version 3.1.19
*******************************************************************************
HPS3D_SDK 更新内容如下:

V1.7.7：
1、融合了障碍物提取算法：支持提取障碍物特征信息值(包含障碍物左端点、右端点、上端点、下端点、最近点的三维空间坐标值,以及障碍物的平均距离、像素点个数等)
使用说明：
	a、使能点云转换--得到点云数据--HPS3D_SetPointCloudEn(true);
	b、配置障碍物提取相关从参数--HPS3D_ObstacleConfigInit(...);
	c、障碍物提取结果保存在MeasureDataTypeDef结构体中的Obstacle_data中
注：如需修改障碍物提取默认配置参数(像素点个数阈值以及阈值偏置)则需使用以下接口：
	设置障碍物像素点个数阈值---HPS3D_SetObstaclePixelNumberThreshold(...);
	获取障碍物像素点个数阈值---HPS3D_GetObstaclePixelNumberThreshold(...);
	设置障碍物提取阈值偏置-----HPS3D_SetThresholdOffset(...);
   	获取障碍物提取阈值偏置-----HPS3D_GetThresholdOffset(...);	
2、新增了获取SDK版本信息接口函数---Version_t HPS3D_GetSDKVersion(...);
注：若固件版本与SDK版本不匹配,请先升级固件后再使用该SDK
3、新增了测量结果特殊值(65300,65400,65500,65530等)配置接口：
   将特殊测量输出值转换为指定特殊值参数配置-----HPS3D_ConfigSpecialMeasurementValue(...);
说明：该接口功能将传感器测量返回的特殊值转换为指定无效测量值;

4、新增了边缘噪声滤除算法,仅需调用设置边缘噪声滤除使能接口函数---HPS3D_SetEdgeDetectionEnable(...);
相关参数配置接口函数(默认即可，一般情况下不需设置以下参数)：
	获取边缘噪声滤除使能 ---extern bool HPS3D_GetEdgeDetectionEnable(void);
	设置边缘噪声阈值 ---extern RET_StatusTypeDef HPS3D_SetEdgeDetectionValue(int32_t threshold_value);
	获取边缘噪声阈值 ---extern int32_t HPS3D_GetEdgeDetectionValue(void);

V1.7.8
1、对点云数据弯曲现象进行优化处理
     ●注：使能点云转换仍出现弯曲现象，请检查光学补偿参数是否使能
     	HPS3D_GetOpticalParamConf(...)----获取光学补偿参数
     	HPS3D_SetOpticalEnable(...)----光学补偿使能设置
     ●点云数据转换仅需使能点云转换即可，使能后数据保存在MeasureData中的point_cloud_data中
		HPS3D_SetPointCloudEn(...) ----点云转换使能设置
2、加入点云数据保存为ply格式文件(可用Meshlab软件进行显示)，便于对点云数据进行分析
    	HPS3D_SavePlyFile(...)  ----保存为ply文件格式点云数据



