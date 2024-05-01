import { createAvatar } from '@dicebear/core'
import { initials } from '@dicebear/collection'

export const generateAvatar = (seed) =>
  createAvatar(initials, {
    seed: seed,
    backgroundColor: ['1677ff'],
    // ... other options
  }).toDataUriSync()