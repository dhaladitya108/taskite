import Cookies from 'js-cookie'
import axios from 'axios'
import applyCaseMiddleware from 'axios-case-converter'

const csrftoken = Cookies.get('csrftoken')

const caseMiddleWareOptions = {
  ignoreHeaders: true,
  preservedKeys: [
    'AWSAccessKeyId',
    'x-amz-algorithm',
    'x-amz-credential',
    'x-amz-date',
    'x-amz-signature',
  ],
}

export const http = applyCaseMiddleware(
  axios.create({
    baseURL: '/api',
    headers: {
      'X-CSRFToken': csrftoken,
    },
  }),
  caseMiddleWareOptions
)
