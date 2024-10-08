# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from typing import List, Union

import numpy as np
import PIL.Image

from ...utils import BaseOutput, is_flax_available


@dataclass
class StableDiffusionXLPipelineOutput(BaseOutput):
  """
  Output class for Stable Diffusion pipelines.

  Args:
      images (`List[PIL.Image.Image]` or `np.ndarray`)
          List of denoised PIL images of length `batch_size` or numpy array of shape `(batch_size, height, width,
          num_channels)`. PIL images or numpy array present the denoised images of the diffusion pipeline.
  """

  images: Union[List[PIL.Image.Image], np.ndarray]


if is_flax_available():
  import flax

  @flax.struct.dataclass
  class FlaxStableDiffusionXLPipelineOutput(BaseOutput):
    """
    Output class for Flax Stable Diffusion XL pipelines.

    Args:
        images (`np.ndarray`)
            Array of shape `(batch_size, height, width, num_channels)` with images from the diffusion pipeline.
    """

    images: np.ndarray
