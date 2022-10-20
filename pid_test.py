import time


class PID:
    """PID Controller
    """

    def __init__(self, P=0.2, I=0.0, D=0.0):  # 设定PID参数调参

        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.clear()

    def clear(self):
        """Clears PID computations and coefficients"""
        self.SetPoint = 5.0
        self.CurrentError = 0.0  # Error[k]
        self.LastError = 0.0  # Error[k-1]
        self.PrevError = 0.0  # Error[k-2]
        self.output = 0.0
        self.Lastoutput = 0.0

    def update(self, feedback_value):
        """Calculates PID value for given reference feedback

        ..Incremental digital PID： 
            u(k)=K_p * ( e[k] - e[k-1] ) + K_i * e[k]  + K_d * ( e[k] - 2* e[k-1] + e[k-2] ) 

        """
        self.CurrentError = self.SetPoint - feedback_value
        # PID calculating
        self.output = self.Lastoutput + self.Kp * (self.CurrentError - self.LastError) + self.Ki * \
            self.CurrentError + self.Kd * \
            (self.CurrentError - 2*self.LastError + self.PrevError)
        self.output += self.output
        # save the old value of error
        self.PrevError = self.LastError
        self.LastError = self.CurrentError
        self.Lastoutput = self.output
        print("Lastoutput:" + str(self.Lastoutput))
        print("Output:" + str(self.output))
        return self.output

    def setKp(self, proportional_gain):
        """Determines how aggressively the PID reacts to the current error with setting Proportional Gain"""
        self.Kp = proportional_gain

    def setKi(self, integral_gain):
        """Determines how aggressively the PID reacts to the current error with setting Integral Gain"""
        self.Ki = integral_gain

    def setKd(self, derivative_gain):
        """Determines how aggressively the PID reacts to the current error with setting Derivative Gain"""
        self.Kd = derivative_gain

    def setWindup(self, windup):
        """Integral windup, also known as integrator windup or reset windup,
        refers to the situation in a PID feedback controller where
        a large change in setpoint occurs (say a positive change)
        and the integral terms accumulates a significant error
        during the rise (windup), thus overshooting and continuing
        to increase as this accumulated error is unwound
        (offset by errors in the other direction).
        The specific problem is the excess overshooting.
        """
        self.windup_guard = windup

    def setSampleTime(self, sample_time):
        """PID that should be updated at a regular interval.
        Based on a pre-determined sampe time, the PID decides if it should compute or return immediately.
        """
        self.sample_time = sample_time


if __name__ == '__main__':
    x_pid = PID(P=0.2, I=0, D=0)
    x_pid.SetPoint = 5
    x_pid.update(10)
    out = x_pid.output
    print(out)
