import { supabaseServer } from './supabase-server';

export async function validateUser(req) {
  const token = req.headers.get('authorization');

  if (!token) {
    throw new Error('Unauthorized');
  }

  const jwt = token.replace('Bearer ', '');

  const {
    data: { user },
    error
  } = await supabaseServer.auth.getUser(jwt);

  if (error || !user) {
    throw new Error('Invalid user');
  }

  return user;
}