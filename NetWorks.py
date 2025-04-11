import skrf as rf
from skrf.data import ring_slot  # noqa: F811
import matplotlib.pyplot as plt


rf.stylely()


# ring_slot.plot_s_db()
ring_slot.plot_s_db(m=0, n=1)
ring_slot.plot_s_db(m=1, n=1)
plt.show()
pass
