# coding: utf-8

"""
    Emby Server REST API
"""

import pprint
import re  # noqa: F401

import six

class ProcessRunMetricsProcessStatistics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current_cpu': 'float',
        'average_cpu': 'float',
        'current_virtual_memory': 'float',
        'current_working_set': 'float',
        'metrics': 'list[ProcessRunMetricsProcessMetricPoint]'
    }

    attribute_map = {
        'current_cpu': 'CurrentCpu',
        'average_cpu': 'AverageCpu',
        'current_virtual_memory': 'CurrentVirtualMemory',
        'current_working_set': 'CurrentWorkingSet',
        'metrics': 'Metrics'
    }

    def __init__(self, current_cpu=None, average_cpu=None, current_virtual_memory=None, current_working_set=None, metrics=None):  # noqa: E501
        """ProcessRunMetricsProcessStatistics - a model defined in Swagger"""  # noqa: E501
        self._current_cpu = None
        self._average_cpu = None
        self._current_virtual_memory = None
        self._current_working_set = None
        self._metrics = None
        self.discriminator = None
        if current_cpu is not None:
            self.current_cpu = current_cpu
        if average_cpu is not None:
            self.average_cpu = average_cpu
        if current_virtual_memory is not None:
            self.current_virtual_memory = current_virtual_memory
        if current_working_set is not None:
            self.current_working_set = current_working_set
        if metrics is not None:
            self.metrics = metrics

    @property
    def current_cpu(self):
        """Gets the current_cpu of this ProcessRunMetricsProcessStatistics.  # noqa: E501

        The current cpu.  # noqa: E501

        :return: The current_cpu of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :rtype: float
        """
        return self._current_cpu

    @current_cpu.setter
    def current_cpu(self, current_cpu):
        """Sets the current_cpu of this ProcessRunMetricsProcessStatistics.

        The current cpu.  # noqa: E501

        :param current_cpu: The current_cpu of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :type: float
        """

        self._current_cpu = current_cpu

    @property
    def average_cpu(self):
        """Gets the average_cpu of this ProcessRunMetricsProcessStatistics.  # noqa: E501

        The average cpu.  # noqa: E501

        :return: The average_cpu of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :rtype: float
        """
        return self._average_cpu

    @average_cpu.setter
    def average_cpu(self, average_cpu):
        """Sets the average_cpu of this ProcessRunMetricsProcessStatistics.

        The average cpu.  # noqa: E501

        :param average_cpu: The average_cpu of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :type: float
        """

        self._average_cpu = average_cpu

    @property
    def current_virtual_memory(self):
        """Gets the current_virtual_memory of this ProcessRunMetricsProcessStatistics.  # noqa: E501

        The currently allocated virtual memory.  # noqa: E501

        :return: The current_virtual_memory of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :rtype: float
        """
        return self._current_virtual_memory

    @current_virtual_memory.setter
    def current_virtual_memory(self, current_virtual_memory):
        """Sets the current_virtual_memory of this ProcessRunMetricsProcessStatistics.

        The currently allocated virtual memory.  # noqa: E501

        :param current_virtual_memory: The current_virtual_memory of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :type: float
        """

        self._current_virtual_memory = current_virtual_memory

    @property
    def current_working_set(self):
        """Gets the current_working_set of this ProcessRunMetricsProcessStatistics.  # noqa: E501

        The currently allocated working set.  # noqa: E501

        :return: The current_working_set of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :rtype: float
        """
        return self._current_working_set

    @current_working_set.setter
    def current_working_set(self, current_working_set):
        """Sets the current_working_set of this ProcessRunMetricsProcessStatistics.

        The currently allocated working set.  # noqa: E501

        :param current_working_set: The current_working_set of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :type: float
        """

        self._current_working_set = current_working_set

    @property
    def metrics(self):
        """Gets the metrics of this ProcessRunMetricsProcessStatistics.  # noqa: E501

        The metrics.  # noqa: E501

        :return: The metrics of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :rtype: list[ProcessRunMetricsProcessMetricPoint]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ProcessRunMetricsProcessStatistics.

        The metrics.  # noqa: E501

        :param metrics: The metrics of this ProcessRunMetricsProcessStatistics.  # noqa: E501
        :type: list[ProcessRunMetricsProcessMetricPoint]
        """

        self._metrics = metrics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProcessRunMetricsProcessStatistics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProcessRunMetricsProcessStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
